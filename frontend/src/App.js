import React from 'react';

import Search from './components/Search';
import Signup from './components/Signup';


const App = () => {
  const token = localStorage.getItem('drspToken');
  return (
    <>
      {token ?
        <Search /> :
        <Signup />
      }
    </>
  );
}

export default App;
