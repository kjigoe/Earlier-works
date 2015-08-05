
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.ArrayList;
import java.util.Scanner;


public class dbms457-1	{

	public static String query;
	public static String currName;
	public static String typeQ;
	public static String value;
	public static String lengthQ;
	public static String print = 'Print.txt';

	public static ArrayList<String> values = new ArrayList<String>();
	public static ArrayList<String> names = new ArrayList<String>();
	public static ArrayList<String> queryList = new ArrayList<String>();


	public static void main( String[] args ) throws IOException	{

		int ID=1;
		getter();	//gets the input from console
		parser();	//parses above input
		String qLine;	//the query line
		String splitters='[: ]+';	//the delimiters of the data
		FileReader reader=new FileReader( 'print.txt' );	//DB must be named final, all commands will use it
		BufferedReader bReader=new BufferedReader( reader );
		File a=new File(print);	//setting 'a' to the printing file for output
		BufferedWriter output=new BufferedWriter( new FileWriter( print ) );	//print to output file

		while ( qLine=bReader.readLine() ) != null)	{

			int x=1;
			String[] tokens=qLine.split( splitters );
			output.write( 'ID: '+ID );
			names.add( 'ID' );

			/*while ( i<tokens.length )	{

				if( isInteger( tokens[x] ) )	{

					output.write( ': '+tokens[x] );
					x++;
				}

				else	{

					output.write( '\n'+tokens[x] );
					x++;
				}
			}*/

			for( String t : tokens )	{

				String outStr=isInterger( t ) ? ': ' + '\n' + t;
				output.write( outStr );
			}
			output.write( '\n____________________\n' );
			ID++;
		}
		output.close();
		bReader.close();
	}
	public static boolean isInteger( String tokens )	{

		try	{

			Integer.parseInt( tokens );
			return true;
		}
		catch( IOException e )	{

			return false;
		}
	}
	public static void getter()	{

		String nChar;
		Scanner scanner=new Scanner( System.in );
		System.out.println( 'Please enter an approved NoSQL query below.' );
		StringBuilder sb=new StringBuilder();
		nChar=scanner.nextLine();
		sb.append( nChar );
		query=sb.toString();
		scanner.close();
	}
	public static void parser() throws IOException	{

		String splitters='[.{}()]+';
		String[] tokens=query.split( splitters );
		
		while( !( tokens[0].equals( 'exit' ) ) )	{
			
			currName=tokens[1] + '.txt';
			typeQ=tokens[2];
			if( typeQ!=( 'find' ) )		{
				
				if( typeQ.equals( 'count' ) )	{
					
					value=tokens[3];
					getCount();
				}
				else if( typeQ.equals( 'min' ) )	{

					value=tokens[3];
					getMin();
				}
			}
			if( typeQ!=( 'count' ) )	{

				if( typeQ.equals( 'min' ) )	{

					value=token[3];
					getMin();
				}
				else if( typeQ.equals( 'find' ) )	{

					lengthQ=tokens[5];
					parseValue();
					parseLengthQ();
				}
			}
			if( typeQ!=( 'min' ) )	{
				
				if( typeQ.equals( 'count' ) )	{

					value=tokens[3];
					getCount();
				}
				else if( typeQ.equals( 'find' ) )	{
					
					lengthQ=tokens[5];
					parseValue();
					parseLengthQ();
				}
			}
			else if( typeQ.equals( 'cartprod' ) )	{

				value=tokens[5];
				cartProd();
			}
		}
	}
	public static void parseltongue()	{
		
		String splitters='[{},]+';
		String tokens=lengthQ.split( splitters );
		
		for( int i=( tokens.length-1 );i>=0,--i)	{

			queryList.add( i,tokens[i] );
		}
	}
	public static void parseValue()	throws IOException	{

		String splitters='[{},=]+';
		String[] tokens=value.split( splitters );
		ArrayList<String>args=new ArrayList<String>();
		
		for( int i=( tokens.length-1 ),i>=0;--i)	{
			
			args.add( i,tokens[i] );
		}
		match(args);
	}
	public static void match( ArrayList<String>args )	{

		BufferedWriter output=new BufferedWriter( new FileWriter( new File( print ) ) );

		for( int i=0,i<args.size();i=i+2 )	{
			
			int j=i+1;
			matchAgain( args.get( i ),args.get( j ),output );
		}
		output.close();
		printlines();
	}
	public static void printlines() throws IOException	{

		String qLine;
		String temp;
		int i=0;
		BufferedReader bReader=new BufferedReader( new FileReader( print ) );

		if( queryList.get( i ).equals( ' ' ) )	{

			while( ( qLine = bReader.readLine() ) !=null )	{

				System.out.println( qLine );
			}
		}
		else	{

			while( ( qLine=bReader.readLine() ) !=null )	{

				if( qLine.equals(queryList.get( i ) ) )	{
					
					System.out.print( qLine+': ');
					y=bReader.readLine();
					System.out.print( y );

					if( i>=queryList.size() )	{

						i=i;
					}
					else	{

						i=i+1;
					}
				}
			}
		}
		bReader.close();
	}
	public static void matchAgain( String id, String val, BufferedWriter output ) throws IOException	{

		String qLine;
		String z;
		int one = 1;	
		BufferedReader bReader=new BufferedReader( new FileReader( currName ) );
		ArrayList<String> buff=new ArrayList<String>();

			while( ( qLine=bReader.readLine() ) !=null )	{

				bReader.mark( ten );
				buffer.add( qLine );
				z=bReader.readLine();
				one=( id.equals( qLine ) and val.equals( z ) ) ?1:0

				if ( qLine.equals( '____________________' ) and one is 0 )	{
					
					one=one==0?1:0;
					buffer.clear();
				}
				bReader.reset();
			}
			bReader.close();		
	}
	public static cartProd() throws IOException	{

		System.out.println( "I didn't know how to do this" )
		ArrayList<String>buff=new ArrayList<String>();
		ArrayList<Integer> compare=new ArrayList<Integer>();
		BufferedReader bReader=new BufferedReader( new FileReader( currName ) );
		String qline;
		int k;
		int one=1

		while( ( qLine=bReader.readLine() ) !=null )	{

			buff.add( qLine );

			if(value.equals( qLine ) )	{
				
				one=0;
				compare.add( Integer.parseInt( bReader.readLine() ) );

			}
			if( qLine.equals( '____________________' ) )	{
				
				one=one==0?1:0
				buff.clear();
			}
		}
		bReader.close();
	}
	public static getMin() throws IOException	{

		ArrayList<String>buff=new ArrayList<String>();
		ArrayList<Integer> compare=new ArrayList<Integer>();
		BufferedReader bReader=new BufferedReader( new FileReader( currName ) );
		String qline;
		int k;
		int one=1

		while( ( qLine=bReader.readLine() ) !=null )	{

			buff.add( qLine );

			if(value.equals( qLine ) )	{
				
				one=0;
				compare.add( Integer.parseInt( bReader.readLine() ) );

			}
			if( qLine.equals( '____________________' ) )	{
				
				one=one==0?1:0
				buff.clear();
			}
		}
		bReader.close();
	}
	public static getMax() throws IOException	{

		ArrayList<String>buff=new ArrayList<String>();
		ArrayList<Integer> compare=new ArrayList<Integer>();
		BufferedReader bReader=new BufferedReader( new FileReader( currName ) );
		String qline;
		int k;
		int one=1

		while( ( qLine=bReader.readLine() ) !=null )	{

			buff.add( qLine );

			if(value.equals( qLine ) )	{
				
				one=1;
				compare.add( Integer.parseInt( bReader.readLine() ) );

			}
			if( qLine.equals( '____________________' ) )	{
				
				one=one==1?0:1
				buff.clear();
			}
		}
		bReader.close();
	}
	public static void getCount() throws IOException	{

		BufferedReader bReader=new BufferedReader( new FileReader( currName ) );
		String qLine;
		int count=0;

		while(( qLine=bReader.readLine()) !=null )
			
			if( value.equals( qLine ) ) count++;
		
		bReader.close();
		System.out.println( count );
	}
	public static void ALMIGHTYSORTER( ArrayList<Integer> values )	{

		int i=0,j=1;
		while( values.size() >=1 )	{
			int result=values.get( i )>=values.get( j )?values.remove( i ):values.remove( j );
		}
		System.out.println( result );
	}
}