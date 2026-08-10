using System;
using System.Collections;
using UnityEngine;

public class TacticalAssetManager : MonoBehaviour
{
    public static TacticalAssetManager Instance;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void LoadDynamicPrefab(string path, Vector3 position, Quaternion rotation, Action<GameObject> onLoaded)
    {
        StartCoroutine(LoadAssetRoutine(path, position, rotation, onLoaded));
    }

    private IEnumerator LoadAssetRoutine(string path, Vector3 position, Quaternion rotation, Action<GameObject> onLoaded)
    {
        ResourceRequest request = Resources.LoadAsync<GameObject>(path);
        yield return request;

        if (request.asset != null)
        {
            GameObject prefab = request.asset as GameObject;
            GameObject instance = Instantiate(prefab, position, rotation);
            onLoaded?.Invoke(instance);
        }
        else
        {
            Debug.LogError($"Failed to load asset at path: {path}");
            onLoaded?.Invoke(null);
        }
    }

    public void UnloadUnusedAssets()
    {
        Resources.UnloadUnusedAssets();
        System.GC.Collect();
    }
}
