import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class MedianFileGenerator {

	private static String[] prefixList = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"};
	private static int prefixLength = prefixList.length;
	private static final String PATH = "d:/median/smallfiles/";
	private static final String BIG_FILE_PATH = "d:/median/bigfiles/";
	private static int prefixIndex = 0;
	
	public static void main(String[] args) {
		
		
		createSmallFiles();
		createBigFile(6250000, 50000000, new ArrayList<>(6250000));
		createBigFile(6250021, 50000000, new ArrayList<>(6250021));
		createBigFile(6250122, 50000000, new ArrayList<>(6250122));
		createBigFile(6250012, 50000000, new ArrayList<>(6250012));
		createBigFile(6248012, 50000000, new ArrayList<>(6248012));
		createBigFile(6248111, 50000000, new ArrayList<>(6248111));
		
		try {
			checkFileValidity(PATH);
			checkFileValidity(BIG_FILE_PATH);
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
	
	private static double getMedianOfFile(String fileName, int lineCount) throws IOException{
		try(BufferedReader reader = new BufferedReader(new FileReader(new File(fileName)))) {
			String line;
			List<Integer> list = new ArrayList<>(lineCount);
			while((line = reader.readLine()) != null) {
				list.add(Integer.valueOf(line));
			}
			Collections.sort(list);
			int index = lineCount / 2;
			if( lineCount % 2 == 0) {
				return (list.get(index) + list.get(index-1)) / 2d;
			} else {
				return (double) list.get(index);
			}
		}
	}
	
	private static String[] getLineCountAndMedian(String fileName){
		fileName = fileName.replace(".txt", "");
		return fileName.split("_");
	}
	
	private static void checkFileValidity(final String path) throws IOException {
		File[] files = new File(path).listFiles();
		for(File f : files) {
			String[] values = getLineCountAndMedian(f.getName());
			double median = getMedianOfFile(f.getAbsolutePath(), (Integer.parseInt(values[0].replaceAll("[a-z]*", ""))));
			System.out.println("Median of " + f.getName() + " is " + median);
		}
	}
	
	private static void createSmallFiles() {
		createSmallFile(5, 2, true);
		createSmallFile(5, 2, true);
		createSmallFile(5, 3, false);
		createSmallFile(5, 3, false);
		createSmallFile(5, 20, true);
		createSmallFile(5, 20, false);
		createSmallFile(4, 2, false);
		createSmallFile(4, 2, true);
		createSmallFile(4, 200, false);
		createSmallFile(4, 200, true);
		createSmallFile(250, 10, false);
		createSmallFile(250, 10, true);
		createSmallFile(250, 5000, false);
		createSmallFile(250, 5000, true);
		createSmallFile(2500, 20, false);
		createSmallFile(2500, 20, true);
		createSmallFile(2500, 10000, false);
		createSmallFile(2500, 10000, true);
		createSmallFile(10000, 80, false);
		createSmallFile(10000, 80, true);
		createSmallFile(10000, 25000, false);
		createSmallFile(10000, 25000, true);
		createSmallFile(150000, 500, false);
		createSmallFile(150000, 500, true);
		createSmallFile(150000, 2500000, false);
		createSmallFile(150000, 2500000, true);
		createSmallFile(2501, 100, false);
		createSmallFile(2501, 100, true);
		createSmallFile(2501, 20000, false);
		createSmallFile(2501, 20000, true);
		createSmallFile(10001, 100, false);
		createSmallFile(10001, 100, true);
		createSmallFile(10001, 25000, false);
		createSmallFile(10001, 25000, true);
		createSmallFile(125001, 500, false);
		createSmallFile(125001, 500, true);
		createSmallFile(125001, 2500000, false);
		createSmallFile(125001, 2500000, true);
		createSmallFile(149999, 500, false);
		createSmallFile(149999, 500, true);
		createSmallFile(149999, 25000, false);
		createSmallFile(149999, 25000, true);
		createSmallFile(123451, 500, false);
		createSmallFile(123498, 500, true);
		createSmallFile(102309, 25000, false);
		createSmallFile(65000, 25000, true);
		createSmallFile(65000, 25000, false);
		createSmallFile(65210, 25000, true);
		createSmallFile(65062, 50000, true);
		createSmallFile(64489, 2500, true);
		createSmallFile(2499, 100, false);
		createSmallFile(2499, 100, true);
		createSmallFile(2499, 100000, false);
		createSmallFile(2499, 100000, true);
		createSmallFile(9999, 5, false);
		createSmallFile(9999, 100, false);
		createSmallFile(9999, 100, true);
		createSmallFile(9999, 25000, false);
		createSmallFile(9999, 25000, true);
		createSmallFile(1300, 10, false);
		createSmallFile(1300, 10, true);
		createSmallFile(1300, 5000, false);
		createSmallFile(1300, 5000, true);
		createSmallFile(62500, 3, false);
		createSmallFile(62500, 100, false);
		createSmallFile(62500, 100, true);
		createSmallFile(62500, 100000, false);
		createSmallFile(62500, 100000, true);
		createSmallFile(62501, 3, false);
		createSmallFile(62501, 100, false);
		createSmallFile(62501, 100, true);
		createSmallFile(62501, 100000, false);
		createSmallFile(62501, 100000, true);
		createSmallFile(62499, 3, false);
		createSmallFile(62499, 100, false);
		createSmallFile(62499, 100, true);
		createSmallFile(62499, 100000, false);
		createSmallFile(62499, 100000, true);
		createSmallFile(33461, 3, false);
		createSmallFile(33461, 100000, false);
		createSmallFile(33544, 100000, true);
		createSmallFile(33544, 100000, false);
		createSmallFile(20006, 50000, true);
		createSmallFile(19987, 50000, true);
		createSmallFile(124987, 100000, true);
		createSmallFile(124988, 100000, false);
		createSmallFile(125048, 50000, true);
		createSmallFile(125147, 50000, true);
		printFileNamesForPythonArray();
	}
	
	private static void printFileNamesForPythonArray() {
		String result = "";
		File file = new File(PATH);
		File[] files = file.listFiles();
		int n = 0;
		boolean dontPrintComma = true;
		for(File f : files) {
			if(dontPrintComma) {
				dontPrintComma = false;
			} else {
				result += ",";
			}
			result += "\"" + f.getName() + "\"";
			n++;
			if(n % 8 == 0) {
				result += ",";
				dontPrintComma = true;
				result += "\n";
			}
		}
		System.out.println(result);
	}
	
	private static void createSmallFile(int size, int range, boolean sorted){
		try {
			List<Integer> list = new ArrayList<>(size);
			Random random = new Random(19);
			for(int i = 0; i < size; i++) {
				if(Math.random() < 0.5) {
					list.add(random.nextInt(range) * -1);
				} else {
					list.add(random.nextInt(range));
				}
			}
			if(sorted) {
				Collections.sort(list);
			}
			String fileName = getMedianOfListAsFileName(size, list, sorted);
			File file = new File(PATH);
			File[] files = file.listFiles();
			if(files != null && files.length > 0) {
				for(File f : files) {
					if(f.getName().equals(fileName)) {
						String prefix;
						int repetition = prefixIndex / prefixLength; 
						int modulus = prefixIndex % prefixLength;
						prefix = prefixList[modulus];
						prefixIndex++;
						for(int i = 0; i < repetition; i++) {
							prefix += prefix;
						}
						fileName = prefix + fileName;
						break;
					}
				}
			}
			BufferedWriter writer = new BufferedWriter(new FileWriter(new File(PATH + fileName)));
			for(int i = 0; i < size; i++) {
				writer.write(String.valueOf(list.get(i)));
				writer.newLine();
			}
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	private static void createBigFile(int size, int range, List<Integer> list){
		try {
			if(list.size() != size) {
				Random random = new Random(19);
				for(int i = 0; i < size; i++) {
					if(Math.random() < 0.5) {
						list.add(random.nextInt(range) * -1);
					} else {
						list.add(random.nextInt(range));
					}
				}
			}
			for(int j = 0; j < 2; j++) {
				String fileName;
				if(j == 0){
					fileName = getMedianOfListAsFileName(size, list, false);
				} else {
					Collections.sort(list);
					fileName = getMedianOfListAsFileName(size, list, true);
				}
				File file = new File(BIG_FILE_PATH);
				File[] files = file.listFiles();
				if(files != null && files.length > 0) {
					for(File f : files) {
						if(f.getName().equals(fileName)) {
							String prefix;
							int repetition = prefixIndex / prefixLength; 
							int modulus = prefixIndex % prefixLength;
							prefix = prefixList[modulus];
							prefixIndex++;
							for(int i = 0; i < repetition; i++) {
								prefix += prefix;
							}
							fileName = prefix + fileName;
							break;
						}
					}
				}
				BufferedWriter writer = new BufferedWriter(new FileWriter(new File(BIG_FILE_PATH + fileName)));
				for(int i = 0; i < size; i++) {
					writer.write(String.valueOf(list.get(i)));
					writer.newLine();
				}
				writer.close();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
}
	
	private static String getMedianOfListAsFileName(final int length, List<Integer> list, boolean sorted) {
		int size = list.size();
		final String prefix = length + "_";
		if(sorted) {
			if(size % 2 == 0) {
				int index = size / 2;
				return prefix + String.valueOf((list.get(index -1) + list.get(index))/2d) + ".txt";
			} else {
				return prefix + String.valueOf(list.get(size/2)) + ".txt";
			}
		} else {
			Integer[] array = list.toArray(new Integer[0]);
			Arrays.sort(array);
			if(size % 2 == 0) {
				int index = size / 2;
				return prefix + String.valueOf((array[index -1] + array[index])/2d) + ".txt";
			} else {
				return prefix + String.valueOf(array[size/2]) + ".txt";
			}
		}
	}
	
}
