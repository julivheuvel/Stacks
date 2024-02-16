import React from 'react'
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <fieldset>
        <legend>Navbar</legend>
        <Link to="/coffee">Home </Link> | 
        <Link to="/coffee/new"> Create</Link>
    </fieldset>
  )
}

export default Navigation;