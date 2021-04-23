import React from 'react';

import './App.css';
import Table from 'rc-table';

import login from './services/authService';



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentData: [
        {
          "name": "Flow 1",
          "number": 75
        },
        {
          "name": "Flow 2",
          "number": 76
        }
      ],
      isLogin: false
    };
    this.ws = new WebSocket("ws://127.0.0.1:5006/");
  }

  login(event) {
    login(name)
    .then((res) =>{
      if (res.ok) {
        this.setState({ isLogin: true })
      }
  };

  render() {


    // this.ws.onopen = () => {
    // //   console.log('Opened Connection!')
    // };

    // this.ws.onmessage = (event) => {
    //   // this.setState({ currentData: JSON.parse(event.data) });
    // };

    // this.ws.onclose = () => {
    // //   console.log('Closed Connection!')
    // };

    const columns = [
      {    
        title: 'Name',
        dataIndex: 'name',
        key: 'name',
        width: 100,
      },
      {    
        title: 'Number',
        dataIndex: 'number',
        key: 'number',
        width: 100,
      }
    ]

    // console.log(this.state.currentData);
    return (
      <div className="App">
        <h1>Dynamic Flow Table</h1>
        <form onSubmit={}>

        </form>
        <button type='submit'>login</button>;
        <Table columns={columns} data={this.state.currentData} />
      </div>
    );
  }
};
export default App;