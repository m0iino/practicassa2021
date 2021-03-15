using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ESBRestaurante.BD;
using ESBRestaurante.Modelos;
// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace ESBRestaurante.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class BusController : ControllerBase
    {
        // GET: api/<BusController>
        [HttpGet]
        public IActionResult Get()
        {
            BDPedido bd = new BDPedido();
            return Ok(bd.obtenerPedido());
        }
        [HttpPost("agregar")]
        public async Task<IActionResult> AgregarPedidoAsync(Pedido nuevo)
        {

            BDPedido bd = new BDPedido();
            await bd.agregarPedidoAsc(nuevo);
            
            return CreatedAtAction(nameof(AgregarPedidoAsync), nuevo);
        }
        [HttpGet("{id}")]
        public async Task<IActionResult> GetPedidoCliente(int id)
        {
            BDPedido bd = new BDPedido();
            var pedido = await bd.obtenerPedidoAsc(id);
            return Ok(pedido);
        }
        [HttpPost("actualizar")]
        public async Task<IActionResult> ActualizarPedido(Pedido actual)
        {
            BDPedido bd = new BDPedido();
            await bd.actualizar(actual);
            return CreatedAtAction(nameof(ActualizarPedido), actual);
        }
    }
}
