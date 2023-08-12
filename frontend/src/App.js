import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react'
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import TodoView from './components/TodoListView';

function App() {
  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState("")
  const [description, setDesc] = useState("")

  // Read all todos
  useEffect(() => {
    axios.get("http://localhost:8000/api/todo")
      .then(res => {
        setTodoList(res.data)
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  })

  // Post a todo
  const addTodoHandler = () => {
    axios.post("http://localhost:8000/api/todo", {"title": title, "description": description})
      .then(res => {
        console.log("Success")
      })
      .catch(error => {
        console.error("Error making request:", error);
      });
  }

  return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">
        Task Manager
      </h1>
      <h6 className="card text-white bg-primary mb-3">
        FastAPI - React - MongoDB
      </h6>
      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">
          Add your Task
        </h5>
        <span className="card-text">
          <input className="mb-2 form-control titleIn" placeholder="Title" onChange={event => setTitle(event.target.value)}/>
          <input className="mb-2 form-control decIn" placeholder="Description" onChange={event => setDesc(event.target.value)}/>
          <button className="btn btn-outline-primary rounded-5 fw-bold mx-2" onClick={addTodoHandler}>
            Add Task
          </button>
        </span>
        <h5 className="card text-white bg-dark mb-3 mt-3">
          Your Tasks
        </h5>
        <div>
          <TodoView todoList={todoList} />
        </div>
        <h6 className="card text-dark bg-warning py-1 mb-0">
          Copyright 2023, All rights reserved &copy;
        </h6>
      </div>
    </div>
  );
}

export default App;
