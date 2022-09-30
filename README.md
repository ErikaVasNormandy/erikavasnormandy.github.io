# techomancer-01.com

A personal site derived from arkadianriver.com and by extension the talented [@ajlkn](http://twitter.com/ajlkn) via http://html5up.net/spectral
Originally this was scavengers-repo, but the upkeep was starting to get in the way and I mainly wanted to focus on art stuff and cyber. 

## Some Notes for Future Me
````
Make sure you keep the CNAME file in mind

bundle install

bundle exec jekyll serve

_ site stuff gets replaced
_ config.yml is the most important aspect
  File | Action
   -----|-------
   **`_config.yml`** | Replace the values for each key with your info.
   **`_data/tokens.yml`** | Create this file, using `_data/tokens-template.yml` as an example.
   **`_data/authors.yml`** | Add author info for yourself as the first entry in the file.

```

## Original arkadian river stuff

- [Features](https://arkadianriver.github.io/arkadianriver.com/topics/user-guide/features.html)
- [Authoring Guide](https://arkadianriver.github.io/arkadianriver.com/topics/user-guide/)


main.scss is where you can actually change the font color of things
      a {
         color: white;
         text-decoration: none;
      }
   }
 
1. Personalize the images with your own, and change the attribution for your new banner
   at the bottom of `_data/credits.yml`.

   Image | Description
   ------|------------
   **`banner.jpg`** | The main large image on the front page
   **`pic01.jpg`** | The topics image
   **`pic02.jpg`** | The works image

1. From the repo's root directory, start Jekyll to preview as you write.
   
   ```
    --future --drafts
   ```
      
1. Open a browser to http://localhost:4000 (or the port number that jekyll indicates to open).


1. Compose your first post!

   ```
   ruby compose.rb
   ```

   The User Guide describes some features that might be useful: http://localhost:4000/topics/user-guide/
