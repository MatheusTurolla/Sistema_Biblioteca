import './CampoTexto.css'

//CRIANDO OS CAMPOS DE TEXTO DO SISTEMA
const CampoTexto = (props) => {
    return(
      <div className="campo-texto">
        <label>{props.label}</label>
        <input placeholder={props.placeholder} />
      </div>
    )
}

export default CampoTexto