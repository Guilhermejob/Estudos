import './App.css'
import { DefaultTemplate } from './Components/DefaultTemplate'
import { Intro } from './Components/Intro'
import { RestaurantSection } from './Components/RestaurantsSection'
import { AboutApp } from './Components/AboutApp'
import { Contact } from './Components/Contact'

function App() {

  return (
    <>
      <DefaultTemplate>
        <Intro/>
        <RestaurantSection/>
        <AboutApp/>
        <Contact/>
      </DefaultTemplate>
    </>
  )
}

export default App
