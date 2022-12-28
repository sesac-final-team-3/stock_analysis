import React from 'react'
import { NavLink } from 'react-router-dom'

const NAV_LINKS = [
  { name: 'News', to: '/news' },
  { name: 'About Us', to: '/about' },
  { name: 'Summery', to: '/summery' },
  { name: 'Finance', to: '/finance' },
]
export function NavLinks({ className }) {
  return (
    <ul className={className}>
      {NAV_LINKS.map((link) => (
        <li key={link.name} className="ml-4">
          <NavLink
            to={link.to}
            className={({ isActive }) =>
              isActive ? 'border-b text-white' : 'text-white hover:border-b'
            }
          >
            {link.name}
          </NavLink>
        </li>
      ))}
    </ul>
  )
}
