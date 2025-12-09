function App() {


  const user = {
    name:'Guilherme',
    module:'m3',
    age:29,
  }

  return (
    <div>
      <lu>
        <li>Nome: {user.name}</li>
        <li>Modulo: {user.module}</li>
        <li>Idade: {user.age}</li>
      </lu>

      <button onClick={() => window.alert(user.name)}>Alerta</button>
    </div>
  )
}

export default App
