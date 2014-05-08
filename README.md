# Git to Perforce Synchronization #

If you use git lcoally but for your corporation you have to have all you commits in Perforce, this tools is going to help you.
It assumes all the work is done in git (and its remotes), so there is no sync back from Perforce to git. 
It saves the last time you Synced, goes through each commit and process it individually: 

- Create the changelist in Perforce
- Checkout the files
- Mark for Add/Delete
- Update the files
- Submit the changelist


## ::warning:: This is a work in progress and not production ready ##