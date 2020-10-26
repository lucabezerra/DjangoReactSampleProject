import React, { useRef } from 'react';

import Button from '../Button';


const Login = props => {
  const username = useRef();
  const password = useRef();

  const submit = () => {
    fetch(
      'http://localhost:8000/api/token/',
      {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          username: username.current.value,
          password: password.current.value,
        }),
      }
    ).then(
      response => response.json().then(responseData => {
        localStorage.setItem("drspToken", responseData.access);
        localStorage.setItem("drspTokenRefresh", responseData.refresh);
        window.location.reload();
      })
    );
  }

  return (
    <div>
      <h2>Login</h2>
      <div>
        <label>Email: </label><input type="text" name="username" ref={username} />
        <label>Password: </label><input type="password" name="password" ref={password} />
        <hr />
        <Button text="Login" onClick={submit} />
      </div>
    </div>
  );
};

export default Login;
