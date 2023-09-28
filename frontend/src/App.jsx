import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// import { ListItem } from './ListItem'

const lista = [
  {
    "id":1,
    "title": "hola a todos",
    "body": "Es un placer acompañarles el dia de hoy",
  },
  {
    "id":2,
    "title": "me voy",
    "body": "Ha sido un largo dia decido irme de una vez",
  },
  {
    "id":3,
    "title": "Hagamos un test",
    "body": "ESto es un test de DRF con React",
  }
]

const Item = ({id, title, body}) => {
  return (
    <div style={{width:'100vw', display:'flex', flexDirection:'column',justifyContent:'space-evenly', margin:'auto'}}>
      <h1>
        <span>{id}</span>
        <span>{title}</span>
      </h1>
      <span>{body}</span>
    </div>
  )
}

function App() {
  const [newLista, setNewLista] = useState([]) 

  useEffect(() => {
    fetch('http://localhost:8000/api/')
    .then(response => response.json())
    .then(data => setNewLista(data))
  }, [])

  return (
    <>
    {
      newLista.map(item => {
        return (
          <Item key={item.id}
                id={item.id}
                title={item.title}
                body={item.body}
          />
        )
      })

    }
    </>
  )
}

export default App
