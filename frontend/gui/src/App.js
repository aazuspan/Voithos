import React from 'react';

import Header from './components/Header';
import InputForm from './components/InputForm';
import MessageList from './containers/MessageList';
import Layout from './containers/Layout';


function App() {
  return (
    <>
      <Layout>
        <Header />
        <MessageList />
        <InputForm />
      </Layout>
    </>
  );
}

export default App;
