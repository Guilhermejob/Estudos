import foto1 from "../../assets/5e6716c9e172f872c52ad470adb3d02d97476aab.jpg"
import foto2 from "../../assets/8dc7dde6da51929e7302ac859a208bffa1a70a68.jpg"
import foto3 from "../../assets/d7203442288251340328c35cbac9e11abc56d012.jpg"
import svgrestaurante from "../../assets/icon_restaurant.svg"
import { CardRestaurante } from "../CardRestaurant"
import styles from "./style.module.css"

export const RestaurantSection = () => {

    const restaurants = [
        {
            id: 1,
            name: 'PizzaPlanet',
            description: 'Lorem Ipsum dolor sit amet',
            foto: foto1
        },
        {
            id: 2,
            name: 'HamBurguer',
            description: 'Lorem Ipsum dolor sit amet',
            foto: foto2
        },
        {
            id: 3,
            name: 'Sushizo',
            description: 'Lorem Ipsum dolor sit amet',
            foto: foto3
        },
    ]

    return (
        <section>
            <div className={styles.container}>
                <div className={styles.titles}>
                    <figure>
                        <img src={svgrestaurante} />
                    </figure>
                    <h2>Restaurantes famosos</h2>
                </div>
                <div className={styles.container_restaurantes}>
                    {restaurants.map(restaurant => {
                        return (
                            <CardRestaurante key={restaurant.id}
                                name={restaurant.name}
                                foto={restaurant.foto}
                                description={restaurant.description}
                            />
                        )
                    })}
                </div>
            </div>
            <div></div>
        </section>
    )
}