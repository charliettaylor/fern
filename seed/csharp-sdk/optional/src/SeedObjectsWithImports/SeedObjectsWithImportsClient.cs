using SeedObjectsWithImports;

#nullable enable

namespace SeedObjectsWithImports;

public partial class SeedObjectsWithImportsClient
{
    private RawClient _client;

    public SeedObjectsWithImportsClient(ClientOptions clientOptions = null)
    {
        _client = new RawClient(
            new Dictionary<string, string>() { { "X-Fern-Language", "C#" }, },
            clientOptions ?? new ClientOptions()
        );
        Optional = new OptionalClient(_client);
    }

    public OptionalClient Optional { get; }

    private string GetFromEnvironmentOrThrow(string env, string message)
    {
        var value = System.Environment.GetEnvironmentVariable(env);
        if (value == null)
        {
            throw new Exception(message);
        }
        return value;
    }
}
