

function App() {

  const fruit_list = [
    {
      "id":1,
      "name":"Morango",
      "category":"vermelha",
      "price":12
    },
    {
      "id":2,
      "name":"Banana",
      "category":"amarela",
      "price":2
    },
    {
      "id":3,
      "name":"Amora",
      "category":"vermelha",
      "price":5
    }
  ]

  return (
    <>
      <ul>
        {fruit_list.map(fruit => {
          return(
            <li key={fruit.id}>
              <h3>Nome: {fruit.name}</h3>
              <p>Categoria: {fruit.category}</p>
              <p>Preço: {fruit.price}</p>
            </li>
          )
        })}
      </ul>
    </>
  )
}

export default App
