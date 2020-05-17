import moment from 'moment'

export interface FollowUpType {
  id: number,
  content: string,
  user: number,
  date: string,
  pennyChat: string,
  url: string,
}


class FollowUp implements FollowUpType {
  id: number
  content: string
  user: number
  date: string
  pennyChat: string
  url: string

  constructor(data: FollowUpType = { id: NaN, content: '', user: NaN, date: '', pennyChat: '', url: '', }) {
    this.id = data.id
    this.content = data.content
    this.date = data.date
    this.user = data.user
    this.url = data.url
    this.pennyChat = data.pennyChat
  }

  get valid(): boolean {
    return !Number.isNaN(this.id)
  }

  get dateFormatted(): string {
    return moment(this.date).format('M/D/YYYY')
  }
}

export default FollowUp