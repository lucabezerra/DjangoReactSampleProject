import React from 'react';

import Login from './components/Login';
import Search from './components/Search';
import Signup from './components/Signup';


const App = () => {
  const token = localStorage.getItem('drspToken');
  return (
    <>
      {token ?
        <Search /> :
        <Login />
      }
    </>
  );
}

export default App;
