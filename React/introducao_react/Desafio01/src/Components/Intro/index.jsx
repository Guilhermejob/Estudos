import foto1 from "../../assets/5e6716c9e172f872c52ad470adb3d02d97476aab.jpg"
import foto2 from "../../assets/8dc7dde6da51929e7302ac859a208bffa1a70a68.jpg"
import foto3 from "../../assets/d7203442288251340328c35cbac9e11abc56d012.jpg"
import styles from "./style.module.css"




export const Intro = () => {
    return (
        <section className={styles.container}>
            <div className={styles.container_info}>
                <header>
                    <h2>Descubra o melhor</h2>
                    <h2>aplicativo de comida</h2>
                </header>
                <p>
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magnam impedit fugiat unde voluptas at cum sint nisi esse expedita exercitationem
                    necessitatibus id
                </p>
                <button>Saiba mais</button>
            </div>
            <div className={styles.container_img}>
                <figure className={styles.img1}>
                    <img src={foto3} />
                </figure>
                <figure className={styles.img2}>
                    <img src={foto1} />
                </figure>
                <figure className={styles.img3}>
                    <img src={foto2} />
                </figure>
                <span className={`${styles.circle} ${styles.c1}`}></span>
                <span className={`${styles.circle} ${styles.c2}`}></span>
                <span className={`${styles.circle} ${styles.c3}`}></span>
            </div>
        </section>
    )
}