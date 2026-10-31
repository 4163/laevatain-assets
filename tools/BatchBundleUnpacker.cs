using System;
using System.IO;
using System.Text.Json;
using System.Collections.Generic;
using System.Threading.Tasks;
using AnimeStudio;

public class BatchItem {
    public string in_ab { get; set; }
    public string out_dir { get; set; }
}

class Program {
    static void Main(string[] args) {
        if (args.Length < 1) {
            Console.WriteLine("Usage: BatchBundleUnpacker <tasks.json>");
            return;
        }
        string tasksPath = args[0];
        string json = File.ReadAllText(tasksPath);
        var items = JsonSerializer.Deserialize<List<BatchItem>>(json);
        Console.WriteLine($"Starting parallel unpack of {items.Count} bundles...");
        
        var sw = System.Diagnostics.Stopwatch.StartNew();
        int completed = 0;
        int failed = 0;
        
        Parallel.ForEach(items, new ParallelOptions { MaxDegreeOfParallelism = Environment.ProcessorCount }, item => {
            try {
                Directory.CreateDirectory(item.out_dir);
                using var reader = new FileReader(item.in_ab);
                var vfs = new VFSFile(reader, item.in_ab, GameType.ArknightsEndfield);
                foreach (var file in vfs.fileList) {
                    string targetPath = Path.Combine(item.out_dir, file.fileName);
                    using var fs = File.Create(targetPath);
                    file.stream.Position = 0;
                    file.stream.CopyTo(fs);
                }
                System.Threading.Interlocked.Increment(ref completed);
            } catch (Exception ex) {
                System.Threading.Interlocked.Increment(ref failed);
                Console.WriteLine($"Failed {item.in_ab}: {ex.Message}");
            }
        });
        
        sw.Stop();
        Console.WriteLine($"Batch unpack complete in {sw.ElapsedMilliseconds} ms. Completed: {completed}, Failed: {failed}");
    }
}
