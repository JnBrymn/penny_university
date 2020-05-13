import { normalize, Schema } from 'normalizr'
import { AnyAction } from 'redux'
// Takes two arrays and returns the union between them as a new array
const union = (a: Iterable<any>, b: Iterable<any>) => (
  [...new Set([...a, ...b])]
)

// Reducer for handling actions that require pagination.
// Requires three types (request, success, and failure),
// and a function to map the pagination to a key, e.g. (action) => action.filterName.
const paginate = ({ types, mapActionToKey }: { types: [string, string, string], mapActionToKey: (action: AnyAction) => string | undefined }) => {
  if (!Array.isArray(types) || types.length !== 3) {
    throw new Error('Expected types to be an array of three elements.')
  }
  if (!types.every((t) => typeof t === 'string')) {
    throw new Error('Expected types to be strings.')
  }
  if (typeof mapActionToKey !== 'function') {
    throw new Error('Expected mapActionToKey to be a function.')
  }

  const [requestType, successType, failureType] = types

  const updatePagination = (state = {
    isFetching: false,
    nextPageUrl: undefined,
    pageCount: 0,
    ids: [],
  }, action: AnyAction) => {
    const { result, responseSchema } = action.payload || {}
    switch (action.type) {
      case requestType:
        return {
          ...state,
          isFetching: true,
        }
      case successType:
        if (responseSchema) {
          const { result: resultIds } = normalize(result, responseSchema)
          return {
            ...state,
            isFetching: false,
            ids: union(state.ids, resultIds),
            nextPageUrl: action.payload?.nextPageUrl,
            pageCount: state.pageCount + 1,
          }
        }
      case failureType:
        return {
          ...state,
          isFetching: false,
        }
      default:
        return state
    }
  }

  return (state = {}, action: AnyAction) => {
    // Update pagination by key
    const key = mapActionToKey(action)
    switch (action.type) {
      case requestType:
      case successType:
      case failureType:
        if (key) {
          return {
            ...state,
            // @ts-ignore
            [key]: updatePagination(state[key], action),
          }
        }
      default:
        return state
    }
  }
}

export default paginate