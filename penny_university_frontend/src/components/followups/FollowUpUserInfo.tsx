import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import { User } from '../../models'

type FollowUpUserInfo = {
  user: User,
  date: string,
  role: 'Organizer' | 'Participant' | ''
}

const FollowUpUserInfo = ({ date, user, role }: FollowUpUserInfo) => (
  <div className="d-flex">
    <div className="bg-secondary mr-2 icon__user">
      <FontAwesomeIcon color="white" size="lg" icon={faUser} />
    </div>
    <div>
      <h6>
        {user.displayName}
        {role === 'Organizer' ? ` - ${role}` : ''}
      </h6>
      <strong className="text-secondary">{date}</strong>
    </div>
  </div>
)

export default FollowUpUserInfo
