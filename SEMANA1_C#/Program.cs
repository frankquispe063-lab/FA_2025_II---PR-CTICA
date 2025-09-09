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
            Console.WriteLine("\"FRANK\"");
        }
        static void ejer3()
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
        static void ejer4()
        {
            Console.Write("Ingrese un número decimal: ");
            double num = Convert.ToDouble(Console.ReadLine());

            double raiz2 = Math.Sqrt(num);
            int redo = (int)Math.Round(num, 0);
            double cubo = Math.Pow(num, 3);
            double raiz3 = Math.Pow(num, 1 / 3d);

            Console.WriteLine("Raiz 2: " + raiz2);
            Console.WriteLine("Redondeado: " + redo);
            Console.WriteLine("Al cubo: " + cubo);
            Console.WriteLine("Raiz 3: " + raiz3);
        }
        static void ejer5()
        {
            Console.Write("Ingrese número: ");
            string num = (Console.ReadLine());

            int entero = int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine("Resto: " + (entero % 2));
            Console.WriteLine("División: "+ (deci))

        }
    }
}
