using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ESBRestaurante.BD;
using System.Threading.Tasks;
using Flurl.Http;
using ESBRestaurante.Modelos;

namespace ESBRestaurante.BD
{
    public class BDPedido
    {
        public static List<Pedido> listaPedidos = new List<Pedido>()
        {
           new Pedido() { Id = 1, Descripcion = "Chalupa" , IdRestaurante = 1, IdRepartidor=1 , IdCliente= 1},
            new Pedido() { Id = 2, Descripcion = "Pizza" , IdRestaurante = 1, IdRepartidor=2 , IdCliente= 2},
            new Pedido() { Id = 3, Descripcion = "Hamburguesa" , IdRestaurante = 1, IdRepartidor=3 , IdCliente=3}

        };

        public IEnumerable<Pedido> obtenerPedido()
        {
            return listaPedidos;
        }

        public async Task<System.Net.Http.HttpResponseMessage> agregarPedidoAsc(Pedido pedido_nuevo)
        {
            var response = await "http://localhost:62499/api/pedido/agregar".PostJsonAsync(pedido_nuevo);
            listaPedidos.Add(pedido_nuevo);
            
            return response;
                        
            
        }
        public async Task<Pedido> obtenerPedidoAsc(int id)
        {
            var url = "http://localhost:62499/api/pedido/" + id.ToString();
            var response = await url.GetJsonAsync<Pedido>();
            return response;
        }
        public async Task actualizar(Pedido actual)
        {
            var response = await "http://localhost:62499/api/pedido/actualizar".PostJsonAsync(actual);
        }
    }
}
