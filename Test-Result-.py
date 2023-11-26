Metoda testiranja crne kutije (Black Box):

1.Testiranje osnovnih aritmetickih operacija :
-sa celim brojevima:
Ulaz:2+5 izlaz:7
Ulaz:4-2 izlaz:2
- negativnim celim brojevima:
Ulaz:-5+3 izlaz:-2
Ulaz:-4-5 izalz:-9
- decimalnim brojevima:
Ulaz:1.2+3.8 izlaz:5
Ulaz:5.9-1.2 izlaz:4.7
-Deljenje sa nulom:
Ulaz:7/0 izlaz:Infitity
Ulaz:-7/0 izlaz:Infitity
-nevazecim karakterima:
Ulaz:6+x izlaz:ERROR 
Ulaz:5^7 izlaz:ERROR
- sa zagradom
Ulaz:2+(3-2) ilzaz:ERROR

Test Jedinicni:
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    @Test
    public void testBasicAddition() {
        String expression = "3+2";
        String expected = "5.0";
        String actual = Calculator.Run(expression);
        assertEquals(expected, actual);
    }
}


Sto se tice greski u samom kodu :
Calculator Java 
linija koda broj 4 Calculator _Calculate
linija 18 i 37 ToString -To Strinlinija oda 183 ne treba RETURN 
Start Java 
8. linija i 37.linija System .out println