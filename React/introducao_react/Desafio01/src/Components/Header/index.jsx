import logo from '../../assets/FoodApp.svg'
import styles from "./style.module.css"

export const Header = () => {
    return (
        <header className={styles.header}>  
            <img src={logo}/>
        </header>
    )
}