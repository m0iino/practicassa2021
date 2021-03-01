using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Restaurante1.Modelos;
using Restaurante1.BD;
namespace Restaurante1.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PedidoController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            BDPedido rpPedido = new BDPedido();
            return Ok(rpPedido.ObtenerPedidos());
        }

        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            BDPedido rpCli = new BDPedido();

            var cliRet = rpCli.ObtenerPedidoCliente(id);

            if (cliRet == null)
            {
                var nf = NotFound("El pedido del cliente " + id.ToString() + " no existe.");
                return nf;
            }

            return Ok(cliRet);

        }

        [HttpPost("agregar")]
        public IActionResult AgregarPedido(Pedido nuevoPedido)
        {
            BDPedido rpCli = new BDPedido();
            rpCli.Agregar(nuevoPedido);
            return CreatedAtAction(nameof(AgregarPedido), nuevoPedido);
        }
        [HttpPost("actualizar")]
        public IActionResult ActualizarPedido(Pedido nuevoPedido)
        {
            BDPedido rpCli = new BDPedido();
            rpCli.Actualizar(nuevoPedido);
            return CreatedAtAction(nameof(AgregarPedido), nuevoPedido);
        }
    }
}
