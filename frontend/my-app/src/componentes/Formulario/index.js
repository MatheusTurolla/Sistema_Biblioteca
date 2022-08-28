import CampoTexto from '../CampoTexto'
import './Formulario.css'

const Formulario = () => {
  return (
    <section className="formulario">
      <form>
        <CampoTexto label="Nome Editora" placeholder="Digite o nome da sua editora" />
        <CampoTexto label="CNPJ" placeholder="Digite o seu CNPJ" />
      </form>
    </section>
  )
}

export default Formulario