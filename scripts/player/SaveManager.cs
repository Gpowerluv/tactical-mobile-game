using System.IO;
using UnityEngine;

[System.Serializable]
public struct PlayerSaveData
{
    public string playerID;
    public int playerLevel;
    public int currencyBalance;
    public float[] lastKnownPosition;
    public string serializedInventoryGrid;
}

public static class SaveManager
{
    private static string SaveFileName => "tactical_save_profile.json";
    private static string SavePath => Path.Combine(Application.persistentDataPath, SaveFileName);

    public static void SaveGame(PlayerSaveData data)
    {
        string json = JsonUtility.ToJson(data, true);
        try
        {
            File.WriteAllText(SavePath, json);
            Debug.Log($"Game successfully saved to: {SavePath}");
        }
        catch (System.Exception e)
        {
            Debug.LogError($"Failed to save game data: {e.Message}");
        }
    }

    public static PlayerSaveData LoadGame()
    {
        if (!File.Exists(SavePath))
        {
            Debug.LogWarning("No save file found. Initializing default profile.");
            return CreateDefaultSaveData();
        }

        try
        {
            string json = File.ReadAllText(SavePath);
            return JsonUtility.FromJson<PlayerSaveData>(json);
        }
        catch (System.Exception e)
        {
            Debug.LogError($"Failed to load save data: {e.Message}");
            return CreateDefaultSaveData();
        }
    }

    private static PlayerSaveData CreateDefaultSaveData()
    {
        return new PlayerSaveData
        {
            playerID = "Operator_Default",
            playerLevel = 1,
            currencyBalance = 1000,
            lastKnownPosition = new float[] { 0f, 0f, 0f },
            serializedInventoryGrid = ""
        };
    }
}
