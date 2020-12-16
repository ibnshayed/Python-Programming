import { useEffect, useState } from "react";
import axios from "axios";

// const data = [
//     {
//       "id":1,
//       "title":"1st todo",
//       "body":"Learn Django properly."
//     },
//     {
//       "id":2,
//       "title":"Second item",
//       "body":"Learn Python."
//     },
//     {
//       "id":3,
//       "title":"Learn HTTP",
//       "body":"It's important."
//     }
//   ]

const App = () => {

  // const [list,setList] = useState(data)
  const [todos, setTodos] = useState(null)

  const getTodos = () =>{
    axios.get('http://127.0.0.1:8000/api/')
         .then(res => setTodos(res.data))
         .catch(error => console.log(error))
  }

  useEffect(() => {
    getTodos()
  },[])

  return (
    <div className="App">
      {
        todos && todos.map(item => (
          <div key={item.id}>
              <h1>{item.title}</h1>
              <p>{item.body}</p>
          </div>
        ))
      }
    </div>
  );
}

export default App;
