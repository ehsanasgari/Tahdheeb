import java.io.*;

public class ParallelTextProcessing {
    public static void main(String[] args) {

        String inputFilePath = args[0];
        String outputFilePath = args[1];

        try {
            System.out.println("Starting process...");

            String jarFilePath = "/alt-asr/yelkheir/LLM_tokenizer/LLM_alignment/farasa_segmenter/FarasaSegmenterJar.jar";
            String[] command = {"java", "-jar", jarFilePath};
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            Process process = processBuilder.start();


            OutputStream outputStream = process.getOutputStream();
            InputStream inputStream = process.getInputStream();

            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(outputStream));
            BufferedReader fileReader = new BufferedReader(new FileReader(inputFilePath));

            BufferedWriter fileWriter = new BufferedWriter(new FileWriter(outputFilePath));

            String line;
            while ((line = fileReader.readLine()) != null) {
                // Write the line to the JAR process
                writer.write(line + "\n");
                writer.flush(); // Flush the writer to send the input

                BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
                String outputLine = reader.readLine();
                if (outputLine != null) {
                    // Write the output line to the output text file
                    fileWriter.write(outputLine + "\n");
                    fileWriter.flush(); // Flush the writer to write immediately
                }
            }

            System.out.println("Closing streams...");
            writer.close();
            inputStream.close();
            outputStream.close();
            fileReader.close();
            fileWriter.close();

            System.out.println("Waiting for the process to finish...");
            int exitCode = process.waitFor();
            System.out.println("Process exited with code " + exitCode);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
