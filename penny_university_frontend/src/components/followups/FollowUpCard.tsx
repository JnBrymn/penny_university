import React, { useState } from 'react'
import { User } from '../../models'
import { Dropdown } from '../../components'
import Content from '../content'
import { EditButton, SaveButton, DeleteButton } from '../buttons'
import modalDispatch from '../modal/dispatch'
import FollowUpUserInfo from './FollowUpUserInfo'
import { FollowUp } from '../../models'
import { FollowUpType } from '../../models/follow-up'

type FollowUpCard = {
  followUp: FollowUp,
  updateFollowUp: (followUp: FollowUpType) => void,
  deleteFollowUp: (followUpID: number) => void,
  canEdit: boolean,
  user: User,
  role: 'Organizer' | 'Participant' | ''
}

const FollowUpButtons = ({ editOnPress, saveOnPress, deleteOnPress, editMode, id }: { deleteOnPress: () => void, editOnPress: () => void, saveOnPress: () => void, editMode: boolean, id: number }) => editMode
  ? <SaveButton className="align-self-start" type="Changes" onClick={saveOnPress} />
  : <Dropdown
      id={`followup-dropdown-${id}`}
      header="Options"
      options={[
        <EditButton className="align-self-start" type="Follow Up" onClick={editOnPress} key={`edit-followup-${id}`} color="link" />,
        <DeleteButton className="align-self-start" type="Follow Up" onClick={deleteOnPress} key={`delete-followup-${id}`} color="link" />
      ]}
    />

const FollowUpCard = ({ followUp, updateFollowUp, deleteFollowUp, canEdit, user, role }: FollowUpCard) => {
  const [editMode, toggleEditMode] = useState(false)
  const [content, updateContent] = useState(followUp.content)

  const saveFollowUp = () => {
    const fllwUp = { ...followUp }
    fllwUp.content = content
    updateFollowUp(fllwUp)
    toggleEditMode(false)
  }

  const deleteOnPress = () => {
    modalDispatch.delete({
      warning: "Are you sure you would like to delete this follow up?",
      confirmOnPress: () => deleteFollowUp(followUp.id)
    })
  }

  const editOnPress = () => toggleEditMode(true)
  return (
    <div className="pt-2">
      <div className="d-flex justify-content-between">
        <FollowUpUserInfo user={user} date={followUp.dateFormatted} role={role} />
        {canEdit ? <FollowUpButtons id={followUp.id} editMode={editMode} saveOnPress={saveFollowUp} editOnPress={editOnPress} deleteOnPress={deleteOnPress} /> : null}
      </div>
      {<Content className="ml-4 border-left pl-3" content={content} onChange={updateContent} editing={editMode} />}
    </div>
  )
}

export default FollowUpCard
