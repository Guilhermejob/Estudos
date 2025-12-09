import styles from "./style.module.css"


export const CardRestaurante = ({ foto, name, description }) => {
    return (
        <div className={styles.card_container}>
            <img src={foto} />
            <div>

                <h4>{name}</h4>
                <p>{description}</p>
            </div>
        </div>
    )
}