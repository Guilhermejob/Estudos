/* eslint-disable no-unused-vars */
import styles from './style.module.css'

export const CardStudent = ({name, age, module}) => {
    return(
        <article className={styles.card}>
            <header className={styles.header}>
                <h3>Nome: {name}</h3>
            </header>
            <section className={styles.section}>
                <p>Idade: {age}</p>
                <p>Modulo: {module}</p>
            </section>
            <footer className={styles.footer}>
                <p>Categoria: Estudante</p>
            </footer>
        </article>
    )
}


