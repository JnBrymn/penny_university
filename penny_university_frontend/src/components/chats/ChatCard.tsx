import React from 'react'
import { Link } from 'react-router-dom'
import {
  Badge,
  Card,
  CardTitle,
} from 'reactstrap'
import Date from '../Date'
import { Content } from '../content'
import ParticipantList from './ParticipantList'
import { Chat } from '../../models'
import moment from 'moment'


type ChatCardProps = {
  chat: Chat | undefined
}

const ChatCard = ({ chat }: ChatCardProps) =>
  chat ? (
    <Card body className="mb-3 border-0 shadow-sm">
      <CardTitle tag="h5" className="d-flex">
        <Link className="text-reset" to={`/chats/${chat.id}`}>{chat.title}</Link>
        {moment(chat.date) > moment() ? <Badge className="ml-2" color="danger">Upcoming</Badge> : null}
      </CardTitle>
      <Date className="text-secondary" date={chat.date} />
      {chat.description
        ? <Content content={chat.description} /> : null}
      <div className="d-flex">
        <ParticipantList className="mr-2" participants={chat.participants} chatID={chat.id} />
      -
      <Link className="ml-2" to={`/chats/${chat.id}`}>
          Follow Ups
      </Link>
      </div>
    </Card>
  ) : null


export default ChatCard
