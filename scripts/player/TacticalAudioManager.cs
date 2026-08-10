using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Audio;

public class TacticalAudioManager : MonoBehaviour
{
    public static TacticalAudioManager Instance;

    [Header("Audio Configuration")]
    [SerializeField] private AudioMixer masterMixer;
    [SerializeField] private int initialPoolSize = 30;
    [SerializeField] private GameObject audioSourcePrefab;

    private Queue<AudioSource> audioPool = new Queue<AudioSource>();
    private Transform poolContainer;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializePool();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void InitializePool()
    {
        poolContainer = new GameObject("AudioPoolContainer").transform;
        poolContainer.SetParent(transform);

        for (int i = 0; i < initialPoolSize; i++)
        {
            CreateNewPooledSource();
        }
    }

    private AudioSource CreateNewPooledSource()
    {
        GameObject obj = Instantiate(audioSourcePrefab, poolContainer);
        AudioSource src = obj.GetComponent<AudioSource>();
        obj.SetActive(false);
        audioPool.Enqueue(src);
        return src;
    }

    public void PlaySpatialSound(AudioClip clip, Vector3 position, float spatialBlend = 1.0f, float volume = 1.0f, float minDistance = 1f, float maxDistance = 50f)
    {
        if (clip == null) return;

        AudioSource source = audioPool.Count > 0 ? audioPool.Dequeue() : CreateNewPooledSource();
        
        source.transform.position = position;
        source.clip = clip;
        source.spatialBlend = spatialBlend;
        source.volume = volume;
        source.minDistance = minDistance;
        source.maxDistance = maxDistance;
        source.rolloffMode = AudioRolloffMode.Logarithmic;
        source.gameObject.SetActive(true);
        source.Play();

        StartCoroutine(ReturnToPoolAfterPlay(source, clip.length));
    }

    private System.Collections.IEnumerator ReturnToPoolAfterPlay(AudioSource source, float delay)
    {
        yield return new WaitForSeconds(delay);
        source.Stop();
        source.clip = null;
        source.gameObject.SetActive(false);
        audioPool.Enqueue(source);
    }
}
