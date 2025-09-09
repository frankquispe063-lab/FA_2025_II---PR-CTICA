using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string nombre, carrera;
            Console.WriteLine("INGRESA TU NOMBRE: ");
            nombre = (Console.ReadLine());
            Console.WriteLine("INGRESA EL NOMBRE DE TU CARRERA: ");
            carrera = (Console.ReadLine());
            //MENSAJE DE BIENVENIDAD
            Console.WriteLine($"\n{nombre}, BIENVENIDOA FUND.ALGORIT{carrera}");
            Console.ReadKey();
        }
        static void ejer2() 
        {
            Console.WriteLine("INGRESA NUMERO X: ");
            int X = int.Parse(Console.ReadLine());

            double resu = (double)X / (double)Y;

            Console.WriteLine("INGRESA NUMERO Y: ");
            int Y = int.Parse(Console.ReadLine());
            Console.WriteLine("SUMA: " + (X + Y));
            Console.WriteLine("RESTA: " + (X - Y));
            Console.WriteLine("MULTIPLICACIÓN: " + (X * Y));
            Console.WriteLine("DIVISIÓN: " + resu);

        }
        static void ejer3()
        {
        }
        static void ejer4()
        {
        }
        static void ejer5()
        {
        }
    }
}
