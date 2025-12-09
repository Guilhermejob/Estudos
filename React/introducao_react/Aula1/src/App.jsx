/* eslint-disable no-unused-vars */


function App() {

  const professor = {
    name:'Guilherme',
    ocupacao:'Programador Front End',
    salario:3800,
  }

  const salvarProfessor = () => {
    console.log(professor)
  }
 

  return (
    <div className="app">
      <h2>{professor.name}</h2>
      <span>Cargo: {professor.ocupacao}</span>
      <span>Salário: R$ {professor.salario}</span>

      <button onClick={salvarProfessor}>Salvar professor</button>
      {/* <button onClick = {() => salvarProfessor(parametro)}>Salvar professor</button>  -> se a nossa função tem parametros executamos ela assim no onClick*/}
    </div>
  )
}

export default App
