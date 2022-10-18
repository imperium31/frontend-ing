import React, { Component, Fragment} from 'react'
import { Button, Modal, ModalHeader, ModalBody } from 'reactstrap'
import NuevoPedido from './NuevoPedido'

class NuevoPedidoModal extends Component {
    state = {
        modal: false
    }

    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }))
    }

    render() {
        
        var titulo = "Añadir Pedido"
        var boton = (<Button color="gray" className="float-right" onClick={this.toggle} style= {{ minWidth: "200px" }}>Añadir</Button>)
        
        return (
            <Fragment>
                {boton}
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>{titulo}</ModalHeader>
                    <ModalBody>
                        <NuevoPedido resetState={this.props.resetState} toggle={this.toggle} Pedido={this.props.pedido}/>
                    </ModalBody>
                </Modal>
            </Fragment>
        )
    }
}

export default NuevoPedidoModal