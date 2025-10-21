using System;
using BIBLITECA_10;

namespace SEMANA_10
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Cajero C = new Cajero();
            int opc;
            string conti;

            do
            {
                Console.WriteLine("BIENVENIDO AL SISTEMA DE CAJERO AUTOMÁTICO\n");
                Console.WriteLine(" 1. CONSULTAR SALDO");
                Console.WriteLine(" 2. DEPOSITAR SALDO");
                Console.WriteLine(" 3. RETIRAR SALDO");
                Console.WriteLine(" 4. SALIR");

                do
                {
                    Console.WriteLine("INGRESE LA OPCIÓN QUE DESEA REALIZAR: ");
                    opc = int.Parse(Console.ReadLine());
                    if (opc <= 0 || opc > 4)
                        Console.WriteLine("ERROR. OPCIÓN NO VÁLIDA. INTENTE DE NUEVO.\n");
                } while (opc <= 0 || opc > 4);

                switch (opc)
                {
                    case 1:
                        Console.WriteLine("SALDO DISPONIBLE: " + C.consultar());
                        break;
                    case 2: C.depositar(0);
                        break;
                    case 3: C.retirar(0);
                        break;
                    case 4:
                        break;
                }

                do
                {
                    Console.WriteLine("\nDESEA CONTINUAR? (S/N): ");
                    conti = Console.ReadLine();

                    if (conti != "S" && conti != "N")
                    {
                        Console.WriteLine("ERROR. SOLO SE PERMITE 'S' O 'N'. ");
                    }
                    else
                    {
                        if (conti == "S")
                        {
                            Console.Clear();
                        }
                        break;
                    }
                } while (true);

            } while (conti == "S");
        }
    }
}