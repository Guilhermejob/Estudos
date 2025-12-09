import { Input } from "../Fragments/Input"
import styles from './style.module.css'


export const Contact = () => {
    return (
        <section className={styles.container}>
            <form>
                <h2>Conheça nosso aplicativo</h2>
                <Input type='text' placeholder='Nome' />
                <Input type='email' placeholder='E-mail' />
                <button type="submit">Saiba mais</button>
            </form>
        </section>
    )
}