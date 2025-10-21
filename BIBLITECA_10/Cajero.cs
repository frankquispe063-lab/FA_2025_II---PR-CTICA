using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BIBLITECA_10
{
    public class Cajero
    {
        double saldo = 1000;

        public double consultar()
        {
            return saldo;
        }
        public void depositar(double monto)
        {
            if (monto > 0)
            {
                Console.WriteLine("\nINGRESE EL MONTO A DEPOSITAR: ");
                string en = Console.ReadLine();
                while (true)
                {
                    try
                    {
                        monto = Convert.ToDouble(en);
                        if (monto > 0)
                        {
                            saldo += monto;
                            Console.WriteLine("DEPOSITO EXITOSO."); break;
                        }
                        else
                        {
                            Console.WriteLine("ERROR. TIENE QUE SER UN DEPOSITO MAYOR A CERO (0)\n");
                            continue;
                        }

                    }
                    catch (FormatException)
                    {
                        Console.WriteLine("ERROR. EL DEPOSITO TIENE QUE SER  UN MONTO VÁLIDO. ");
                        continue;
                    }
                }
            }
        }
        public void retirar(double monto)
        {
            if (monto > 0)
            {
                Console.WriteLine("\nINGRESE EL MONTO A DEPOSITAR: ");
                string en = Console.ReadLine();
                while (true)
                {
                    try
                    {
                        monto = Convert.ToDouble(en);
                        if (monto <= saldo)
                        {
                            saldo -= monto;
                            Console.WriteLine("RETIRO EXITOSO."); break;
                        }else if (monto > 0)
                        {
                            Console.WriteLine("ERROR. TIENE QUE SER UN DEPOSITO MAYOR A CERO (0)\n");
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("ERROR. SALDO INSUFICIENTE\n");
                            continue;
                        }

                    }
                    catch (FormatException)
                    {
                        Console.WriteLine("ERROR. EL DEPOSITO TIENE QUE SER  UN MONTO VÁLIDO. ");
                    }
                }
            }
        }
    }
}
