import React from 'react';

import Header from './components/Header';
import InputForm from './components/InputForm';
import MessageList from './containers/MessageList';


function App() {
  return (
    <>
      <Header />
      <MessageList />
      <InputForm />
    </>
  );
}

export default App;
