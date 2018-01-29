## Problem: Given strings assigment\_1 and assignment\_2, shown below, use string indexing to extract the due dates of each assignment and print the due dates, separated by a comma and a space.
    assignment_1 = "Maze Game,Jan. 26,10pts"
	assignment_2 = "Types,Feb. 2,10pts"
### Step 1: Find the indexes of each due date.
<table>
	<tr>
		<th>0</th>
		<th>1</th>
		<th>2</th>
		<th>3</th>
		<th>4</th>
		<th>5</th>
		<th>6</th>
		<th>7</th>
		<th>8</th>
		<th>9</th>
		<th>10</th>
		<th>11</th>
		<th>12</th>
		<th>13</th>
		<th>14</th>
		<th>15</th>
		<th>16</th>
		<th>17</th>
		<th>18</th>
		<th>19</th>
		<th>20</th>
		<th>21</th>
		<th>22</th>
	</tr>
	<tr>
		<td>M</td>
		<td>a</td>
		<td>z</td>
		<td>e</td>
		<td> </td>
		<td>G</td>
		<td>a</td>
		<td>m</td>
		<td>e</td>
		<td>,</td>
		<td>J</td>
		<td>a</td>
		<td>n</td>
		<td>.</td>
		<td> </td>
		<td>2</td>
		<td>6</td>
		<td>,</td>
		<td>1</td>
		<td>0</td>
		<td>p</td>
		<td>t</td>
		<td>s</td>
	</tr>
</table>

We can see that the due date for assignment_1 (Jan. 26) starts at index 10 and ends at index 16. Therefore to include the entire date with string indexing we need to put 

	assignment_1[10:17]
because python stops at the character before the index given by the second number. 

Doing the same thing for assignment_2 we can see we need to use 

	assignment_2[6:11]

<table>
	<tr>
		<th>0</th>
		<th>1</th>
		<th>2</th>
		<th>3</th>
		<th>4</th>
		<th>5</th>
		<th>6</th>
		<th>7</th>
		<th>8</th>
		<th>9</th>
		<th>10</th>
		<th>11</th>
		<th>12</th>
		<th>13</th>
		<th>14</th>
		<th>15</th>
		<th>16</th>
		<th>17</th>
	</tr>
	<tr>
		<td>T</td>
		<td>y</td>
		<td>p</td>
		<td>e</td>
		<td>s</td>
		<td>,</td>
		<td>F</td>
		<td>e</td>
		<td>b</td>
		<td>.</td>
		<td> </td>
		<td>2</td>
		<td>,</td>
		<td>1</td>
		<td>0</td>
		<td>p</td>
		<td>t</td>
		<td>s</td>
	</tr>
</table> 

### Step 2: Print out the due dates, separated by commas. 
We know we can use the + operator to concatenate (combine) strings. This can be done directly in the print statement. So 

	print(assignment_1[10:17] + assignment_2[6:11]) 
will print out 

	Jan. 26Feb. 2

But this isn't exactly what we want. We can also concatenate string literals using the + operator. String literals are any string values in quotation marks. So `assignment_1` is a variable, while `"Maze Game,Jan. 26,10pts"` is the string literal value we store in the variable. So with that in mind, we can use 

	print(assignment_1[10:17] + ", " + assignment_2[6:11]) #Notice the space!
which will print out 
	
	Jan. 26, Feb. 2
