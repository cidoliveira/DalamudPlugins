# cidoliveira — Dalamud plugins

Repositório pessoal de plugins Dalamud. / Personal Dalamud plugin repository.

## Instalar / Install

Adicione esta URL em Dalamud → Settings → Experimental → **Custom Plugin Repositories**,
marque *Enabled* e salve. Os plugins aparecem no `/xlplugins`.

Add this URL in Dalamud → Settings → Experimental → **Custom Plugin Repositories**,
tick *Enabled* and save. The plugins then show up in `/xlplugins`.

```
https://raw.githubusercontent.com/cidoliveira/DalamudPlugins/main/pluginmaster.json
```

## Plugins

| Plugin | Código / Source | Notas / Notes |
|---|---|---|
| **Lazarek** | [cidoliveira/AnoMech](https://github.com/cidoliveira/AnoMech/tree/feat/plugin-compat) | Fork do [AnoMech](https://github.com/anomek/AnoMech) com Splatoon, BossMod e NyaDraw nas simulações. Desinstale o AnoMech original antes. |

## Adicionar um plugin / Adding a plugin

1. Publique o `latest.zip` do plugin num release do repositório dele.
2. Crie `plugins/<Nome>.json` com o manifesto empacotado do plugin (o `<InternalName>.json` que sai
   junto do `latest.zip`) mais `DownloadLinkInstall` apontando para o zip do release.
3. Coloque o ícone em `icons/` e aponte o `IconUrl` para
   `https://raw.githubusercontent.com/cidoliveira/DalamudPlugins/main/icons/<arquivo>`.
4. Faça o push: a Action regenera o `pluginmaster.json`. Localmente: `python tools/build_pluginmaster.py`.

Para o Dalamud oferecer uma atualização, o `AssemblyVersion` precisa subir.
