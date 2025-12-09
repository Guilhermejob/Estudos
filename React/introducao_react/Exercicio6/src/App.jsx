/* eslint-disable no-unused-vars */
import './App.css'
import { CardStudent } from './Components/CardStudent'

function App() {

  const student = {
    "name":'Guilherme',
    "age":29,
    "module":"M3"
  }


  return (
    <>
       <CardStudent name={student.name} age={student.age} module={student.module}/>
    </>
  )
}

export default App
