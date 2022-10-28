<?php function print_pattern($num) { 
// Outer loop handles number of rows 
for ($i = 1; $i <= $num; $i++) { 
// inner loop handles indentation 
for($k = $num; $k > $i; $k-- ) { 
// Print spaces 
echo " "; 
} 
// inner loop handles number of stars 
for($j = 1; $j <= $i; $j++ ) { 
// Print characters 
echo chr(64+$j)." "; 
} 
for($j = $i-1; $j >= 1; $j-- ) { 
// Print characters 
echo chr(64+$j)." "; 
} 
// go to new line after each row pattern is printed 
echo "<br>"; 
} 
} //Call function and send number of lines as parameter 
$num = 5; print_pattern($num); 
?> 
