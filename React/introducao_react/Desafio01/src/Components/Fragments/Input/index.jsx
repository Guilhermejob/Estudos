import style from './style.module.css'


export const Input = ({type,placeholder}) => {
    return(
        <fieldset>
            <input className={style.input} type={type} placeholder={placeholder}/>
        </fieldset>
    )
}