using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Restaurante1.Modelos;
namespace Restaurante1.BD
{
    public class BDPedido
    {
        public static List<Pedido> listaPedidos = new List<Pedido>()
        {
            new Pedido() { Id = 1, Descripcion = "Chalupa" , IdRestaurante = 1, IdRepartidor=1 , IdCliente= 1},
            new Pedido() { Id = 2, Descripcion = "Pizza" , IdRestaurante = 1, IdRepartidor=2 , IdCliente= 2},
            new Pedido() { Id = 3, Descripcion = "Hamburguesa" , IdRestaurante = 1, IdRepartidor=3 , IdCliente=3}

        };


        public IEnumerable<Pedido> ObtenerPedidos()
        {
            return listaPedidos;
        }

        public Pedido ObtenerPedidoCliente(int id)
        {
            var pedido = listaPedidos.Where(ped => ped.IdCliente == id);

            return pedido.FirstOrDefault();
        }

        public void Agregar(Pedido nuevoPedido)
        {
            listaPedidos.Add(nuevoPedido);
        }

        public void Actualizar(Pedido nuevoPedido)
        {
            var found = listaPedidos.FirstOrDefault(c => c.Id == 1);
            found.estado = 1;
            foreach (var item in listaPedidos)
            {
                Debug.WriteLine(item.estado);

            }
            //Debug.ReadLine();
              
            //listaPedidos.Select(c => { c.estado = nuevoPedido.estado; return c; }).ToList();
        }
    }
}
