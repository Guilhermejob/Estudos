import icon_smartphone from '../../assets/icon_smartphone.svg'
import styles from './style.module.css'

export const AboutApp = () => {
    return (
        <section className={styles.container}>
            <div className={styles.container_info}>
                <img src={icon_smartphone} />
                <h2>Sobre o</h2>
                <h2>aplicativo</h2>
            </div>
            <div className={styles.container_info}>
                <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia aliquam quos totam porro architecto reiciendis nulla ducimus, 
                    maiores placeat harum numquam blanditiis ipsam at sunt itaque esse? Quis, consequuntur maxime Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                    Sint sed labore est obcaecati mollitia quis maxime architecto sequi? Illum recusandae a quae, debitis tenetur assumenda odit ab omnis cumque asperiores!
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia aliquam quos totam porro architecto reiciendis nulla ducimus, 
                    maiores placeat harum numquam blanditiis ipsam at sunt itaque

                </p>
            </div>
        </section>
    )
}