import React, { useRef } from 'react';

import Button from '../Button';


const Signup = props => {
  const email = useRef();
  const password = useRef();
  const firstName = useRef();
  const lastName = useRef();

  const submitForm = () => {
    fetch(
      'http://localhost:8000/core/user/',
      {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          email: email.current.value,
          password: password.current.value,
          first_name: firstName.current.value,
          last_name: lastName.current.value,
          username: email.current.value,
        }),
      }
    ).then(
      response => response.json().then(responseData => {
        console.log(responseData);
      })
    );
  }

  return (
    <div>
      <h2>Signup</h2>
      <div>
        <label>Email: </label><input type="text" name="email" ref={email} />
        <label>Password: </label><input type="password" name="password" ref={password} />
        <hr />
        <label>First Name: </label><input type="text" name="first_name" ref={firstName} />
        <label>Last Name: </label><input type="text" name="last_name" ref={lastName} />

        <Button text="Send" onClick={submitForm} />
      </div>
    </div>
  );
};

export default Signup;
